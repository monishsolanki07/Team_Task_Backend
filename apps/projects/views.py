from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Project, ProjectMembership


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_project(request):
    # 🔐 Only system admin can create project
    if not request.user.is_staff:
        return Response({"error": "Only admin can create project"}, status=403)

    project = Project.objects.create(
        name=request.data.get('name'),
        created_by=request.user
    )

    ProjectMembership.objects.create(
        user=request.user,
        project=project,
        role='ADMIN'
    )

    return Response({"msg": "project created", "id": project.id})


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