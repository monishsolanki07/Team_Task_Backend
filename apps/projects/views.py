from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Project, ProjectMembership


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_project(request):
    if not request.user.is_staff:
        return Response({"error": "Only admin can create project"}, status=403)

    project = Project.objects.create(
        name=request.data.get('name'),
        description=request.data.get('description', ''),
        created_by=request.user
    )

    # creator = ADMIN
    ProjectMembership.objects.create(
        user=request.user,
        project=project,
        role='ADMIN'
    )

    # add members
    members = request.data.get('members', [])

    for user_id in members:
        if not ProjectMembership.objects.filter(user_id=user_id, project=project).exists():
            ProjectMembership.objects.create(
                user_id=user_id,
                project=project,
                role='MEMBER'
            )

    return Response({
        "msg": "project created",
        "id": project.id
    })


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_member(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    # 🔐 Check admin
    if not ProjectMembership.objects.filter(
        user=request.user, project=project, role='ADMIN'
    ).exists():
        return Response({"error": "Not admin"}, status=403)

    user_id = request.data.get('user_id')

    # ⚠️ Prevent duplicate membership
    if ProjectMembership.objects.filter(user_id=user_id, project=project).exists():
        return Response({"error": "User already in project"}, status=400)

    ProjectMembership.objects.create(
        user_id=user_id,
        project=project,
        role='MEMBER'
    )

    return Response({"msg": "member added"})

from apps.tasks.models import Task

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    memberships = ProjectMembership.objects.filter(project=project).select_related('user')
    tasks = Task.objects.filter(project=project).select_related('assigned_to')

    data = {
        "id": project.id,
        "name": project.name,
        "description": project.description,
        "created_by": project.created_by.username,
        "created_at": project.created_at,

        "members": [
            {
                "id": m.user.id,
                "username": m.user.username,
                "role": m.role
            }
            for m in memberships
        ],

        "total_tasks": tasks.count(),

        "tasks": [
            {
                "id": t.id,
                "title": t.title,
                "status": t.status,
                "assigned_to": t.assigned_to.username if t.assigned_to else None,
                "due_date": t.due_date
            }
            for t in tasks
        ]
    }

    return Response(data)