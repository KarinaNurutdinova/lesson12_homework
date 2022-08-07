import json


def load_posts() -> list[dict]:
    with open('posts.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def search_tag(tag: str) -> list[dict]:
    search_result = []
    for post in load_posts():
        if tag.lower() in post["content"].lower():
            search_result.append(post)
    return search_result


def append_post(post: dict) -> dict:
    posts = load_posts()
    posts.append(post)
    with open("posts.json", 'w', encoding='utf-8') as file:
        json.dump(posts, file)
    return post
