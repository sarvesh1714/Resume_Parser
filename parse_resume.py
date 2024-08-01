import json

def parse_resume(resume_text):
    # Example parsing logic (customize based on your resume format)
    resume_data = {
        "Name": "John Doe",
        "Contact Information": {
            "Email": "john.doe@example.com",
            "Phone": "123-456-7890"
        },
        "Education": [
            {
                "Institution": "XYZ University",
                "Degree": "Bachelor of Science in Computer Science",
                "Year": "2024"
            }
        ],
        "Work Experience": [
            {
                "Job Title": "Software Engineer Intern",
                "Company": "ABC Corp",
                "Dates": "June 2023 - August 2023",
                "Responsibilities": "Developed and maintained web applications."
            }
        ],
        "Skills": ["Python", "JavaScript", "Machine Learning"],
        "Certifications": ["Certified Python Developer"],
        "Projects": [
            {
                "Project Title": "Adaptive Traffic Management System",
                "Description": "A system using AI to optimize traffic flow."
            }
        ]
    }
    
    return json.dumps(resume_data, indent=4)

if __name__ == "__main__":
    # Replace with the actual resume text
    resume_text = """..."""
    parsed_resume = parse_resume(resume_text)
    print(parsed_resume)
