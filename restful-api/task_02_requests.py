#!/usr/bin/python3
"""
task_02_requests.py
Fetch posts from JSONPlaceholder using requests,
print titles, and save selected fields to posts.csv.
"""

import csv
import requests


URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    """Fetch all posts and print status code + titles."""
    try:
        response = requests.get(URL, timeout=10)
    except requests.RequestException:
        # في حال فشل الاتصال/الطلب
        print("Status Code: None")
        return

    print(f"Status Code: {response.status_code}")

    if response.status_code != 200:
        return

    posts = response.json()
    for post in posts:
        # طباعة عنوان كل بوست
        print(post.get("title", ""))


def fetch_and_save_posts():
    """Fetch all posts and save id/title/body into posts.csv."""
    try:
        response = requests.get(URL, timeout=10)
    except requests.RequestException:
        print("Status Code: None")
        return

    if response.status_code != 200:
        return

    posts = response.json()

    # تحويل البيانات إلى قائمة dicts فيها فقط المفاتيح المطلوبة
    simplified_posts = [
        {
            "id": post.get("id"),
            "title": post.get("title", ""),
            "body": post.get("body", ""),
        }
        for post in posts
    ]

    # كتابة CSV
    fieldnames = ["id", "title", "body"]
    with open("posts.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(simplified_posts)
