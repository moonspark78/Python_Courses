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
    print("-" * 30)
    print(archive["content"])
    print("=" * 30)
    
    
def save_archive(archive):
    filename = f"{archive['id']}.txt"
    with open(filename, "w", encoding="utf-8") as file:
        file.write(archive["title"] + "\n")
        file.write(archive["content"] + "\n")
        file.write(archive["status"])
    print(f"Archive sauvegardee : {filename}")
    
def main():
    title = "Python et automatisation"
    content = "Python permet d'automatiser des taches."
    archive = generate_archive(title, content)
    display_archive(archive)
    save_archive(archive)
    
if __name__ == "__main__":
    main()