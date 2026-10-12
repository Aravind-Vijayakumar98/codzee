from rest_framework import status
from rest_framework.test import APITestCase
from .models import Task

class TaskAPITests(APITestCase):
    def test_create_task(self):
        response = self.client.post("/api/tasks/", {
            "title": "Prepare assessment",
            "description": "Create meaningful PRs",
            "status": "todo",
            "priority": "high",
        }, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)

    def test_title_is_trimmed(self):
        response = self.client.post("/api/tasks/", {
            "title": "  Review code  ",
        }, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], "Review code")

    def test_blank_title_is_rejected(self):
        response = self.client.post("/api/tasks/", {"title": "   "}, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_status_is_rejected(self):
        response = self.client.post("/api/tasks/", {
            "title": "Valid title",
            "status": "blocked",
        }, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_list_tasks(self):
        Task.objects.create(title="First")
        response = self.client.get("/api/tasks/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_health_check(self):
        response = self.client.get("/api/health/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["status"], "ok")
