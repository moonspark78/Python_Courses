import textwrap
import uuid

def generate_archive(title, content):
    archive_id = str(uuid.uuid4())[:8]
    formatted_content = textwrap.fill(content, width=50)
    archive = {
        "id": archive_id,
        "title": title,
        "content": formatted_content,
        "status": "created"
    }
    return archive

def display_archive(archive):
    print("=" * 30)
    print(f"Archive : {archive['title']}")
    print(f"Identifiant : {archive['id']}")
    print(f"Statut : {archive['status']}")