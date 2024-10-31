
# PROJECT1337

A brief demonstration of Celery, Redis, and Flower.

---

## Getting Started

1. **Clone the Repository:**
   ```bash
   git clone <https://github.com/matpvl/project1337.git>
   cd <project1337>
   ```

---

## Installation

1. **Install Poetry:**  
   Follow the instructions [here](https://python-poetry.org/docs/#installation).

2. **Activate Poetry Environment:**
   ```bash
   poetry install
   poetry shell
   ```

---

## Development Workflow

1. **Run Build Script (it's important to run the build locally before pushing changes):**
   ```bash
   invoke build-local
   ```

2. **Format Code with Black:**
   ```bash
   invoke black
   ```

---

## Prerequisites

1. **Docker / Docker-Compose**  
   - Make sure Docker is installed: [Docker Installation Guide](https://docs.docker.com/get-docker/).  
   - Depending on your platform, you might need to use `docker-compose` instead of `docker compose`. The `invoke` tasks will attempt to detect the correct command automatically.

---

## Running the Application

1. **Build and Start Services with Docker:**
   Instead of manually running `docker compose`, use the following `invoke` task:

   ```bash
   invoke buildup
   ```

   This will:
   - Build the Docker image.
   - Start the services.

2. **Access the Main Application:**
   Visit the following endpoint in your browser:

   - **Main App Endpoint:**  
     [http://localhost:8000/contact-person/](http://localhost:8000/contact-person/)

   - Enter a phone number in the input field. This will store the contact and track its status.

3. **Inspect Stored Contacts in the Python Shell:**
   Use the following command to open a Python shell inside the Docker container:

   ```bash
   invoke docker_shell
   ```

   In the shell, you can query the `TargetedContact` objects to inspect their status and other fields:

   ```python
   from app.models import TargetedContact  # Adjust import path if needed
   contacts = TargetedContact.objects.all()
   for contact in contacts:
       print(contact.phone_number, contact.status)
   ```

4. **Monitor Celery Workers with Flower:**
   Flower is available at:

   - **Flower Dashboard:**  
     [http://localhost:5555/](http://localhost:5555/)

---

## Troubleshooting

- **Docker Command Issues:**  
  If Docker commands fail, ensure either `docker compose` or `docker-compose` is installed. The `invoke` tasks will try both and use the one that works.

- **Logs:**  
  Check the logs for more details if you encounter issues:

  ```bash
  docker compose logs -f  # or 'docker-compose logs -f'
  ```

---

## Conclusion

With this setup, you can:
1. Build and run the app using `invoke buildup`.
2. Enter phone numbers at [http://localhost:8000/contact-person/](http://localhost:8000/contact-person/).
3. Inspect stored contacts via the Python shell (`invoke docker_shell`) or on the /contact-person/ endpoint.
4. Monitor Celery workers with Flower ([http://localhost:5555/](http://localhost:5555/)).
