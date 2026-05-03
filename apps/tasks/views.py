from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.utils.timezone import now
from collections import defaultdict
from .models import TaskActivity
from .models import Task
from apps.projects.models import ProjectMembership, Project


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_task(request):
    project = get_object_or_404(Project, id=request.data.get('project_id'))

    # 🔐 Only project admin can create task
    if not ProjectMembership.objects.filter(
        user=request.user, project=project, role='ADMIN'
    ).exists():
        return Response({"error": "Not admin"}, status=403)

    assigned_to = request.data.get('assigned_to')

    # ⚠️ Ensure user belongs to project
    if not ProjectMembership.objects.filter(
        user_id=assigned_to, project=project
    ).exists():
        return Response({"error": "User not in project"}, status=400)

    task = Task.objects.create(
        title=request.data.get('title'),
        description=request.data.get('description'),
        due_date=request.data.get('due_date'),
        assigned_to_id=assigned_to,
        project=project
    )
    TaskActivity.objects.create(
        task=task,
        user=request.user,
        action="Task created"
   )

    return Response({"msg": "task created", "id": task.id})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def my_tasks(request):
    tasks = Task.objects.filter(assigned_to=request.user).select_related('project')

    data = [
        {
            "id": t.id,
            "title": t.title,
            "status": t.status,
            "due_date": t.due_date,
            "project": t.project.name
        }
        for t in tasks
    ]

    return Response(data)


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update_task(request, id):
    task = get_object_or_404(Task, id=id)

    # 🔐 Only assigned user can update
    if task.assigned_to != request.user:
        return Response({"error": "Not allowed"}, status=403)

    new_status = request.data.get('status')

    # ⚠️ Validate status
    if new_status not in ['TODO', 'IN_PROGRESS', 'DONE']:
        return Response({"error": "Invalid status"}, status=400)

    task.status = new_status
    task.save()
    TaskActivity.objects.create(
        task=task,
        user=request.user,
        action=f"Status changed to {task.status}"
    )

    return Response({"msg": "updated"})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def dashboard(request):
    tasks = Task.objects.filter(assigned_to=request.user)

    return Response({
        "total": tasks.count(),
        "completed": tasks.filter(status='DONE').count(),
        "pending": tasks.filter(status='TODO').count(),
        "overdue": tasks.filter(due_date__lt=now()).count()
    })


# 📅 BONUS: Calendar API
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def calendar_view(request):
    tasks = Task.objects.filter(assigned_to=request.user)

    grouped = defaultdict(list)

    for t in tasks:
        date = t.due_date.date().isoformat()
        grouped[date].append({
            "id": t.id,
            "title": t.title,
            "status": t.status
        })

    return Response(grouped)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def task_activity(request, task_id):
    activities = TaskActivity.objects.filter(task_id=task_id).order_by('-timestamp')

    data = [
        {
            "action": a.action,
            "user": a.user.username,
            "time": a.timestamp
        }
        for a in activities
    ]

    return Response(data)