from app_with_blueprints import create_app
app = create_app()
app.run(host="127.0.0.1", port=5002, debug=True)
