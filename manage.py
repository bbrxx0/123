import click
from app import create_app, db
from app.models import User, Hotel, Room

app = create_app()

@click.group()
def cli():
    pass

@cli.command("init-db")
def init_db():
    with app.app_context():
        db.create_all()
    click.echo("Database initialized.")

@cli.command("create-admin")
@click.option("--email", required=True, help="Admin email")
@click.option("--password", required=True, help="Admin password")
def create_admin(email, password):
    with app.app_context():
        db.create_all()
        email = email.lower().strip()
        if User.query.filter_by(email=email).first():
            click.echo("User already exists.")
            return
        user = User(email=email, is_admin=True, is_email_confirmed=True)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        click.echo(f"Created admin: {email}")

@cli.command("seed")
def seed():
    """Create 9 hotels in Poland + sample rooms."""
    from app.seed_data import seed_poland_hotels
    with app.app_context():
        db.create_all()
        seed_poland_hotels()
        click.echo("Seed data created (9 hotels).")

@cli.command("run")
def run():
    app.run(debug=True)

if __name__ == "__main__":
    cli()
