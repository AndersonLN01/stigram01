from flask import Flask, render_template, url_for
import os

app = Flask(__name__)

@app.route("/")
def index():
    base_path = os.path.join(app.static_folder, "stickers")
    stickers = []

    # Verifica se a pasta existe para evitar erros
    if os.path.exists(base_path):
        for category in os.listdir(base_path):
            category_path = os.path.join(base_path, category)
            if os.path.isdir(category_path):
                for filename in os.listdir(category_path):
                    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.webp', '.gif')):
                        file_url = url_for('static', filename=f'stickers/{category}/{filename}')
                        stickers.append({
                            "url": file_url,
                            "categoria": category.lower()
                        })

    return render_template("index.html", stickers=stickers)

if __name__ == "__main__":
    # O debug=True faz o servidor reiniciar automaticamente ao salvar mudanças
    app.run(debug=True)
