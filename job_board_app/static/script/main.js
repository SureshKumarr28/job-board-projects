document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('jobApplicationForm');

    form.addEventListener('submit', async (e) => {
        e.preventDefault(); // Prevent default form submission

        // Get form data
        const fullName = document.getElementById('fullName').value;
        const email = document.getElementById('email').value;
        const resumeFile = document.getElementById('resume').files[0];

        // Validate form fields (you can add custom validation logic here)

        // Create FormData object to send data via AJAX
        const formData = new FormData();
        formData.append('fullName', fullName);
        formData.append('email', email);
        formData.append('resume', resumeFile);

        try {
            // Send form data to server using fetch API
            const response = await fetch('/submit_application', {
                method: 'POST',
                body: formData
            });

            if (!response.ok) {
                throw new Error('Failed to submit application');
            }

            const result = await response.text();
            console.log(result); // Log server response

            // Optionally display success message to user
            alert('Application submitted successfully!');
            // Redirect to another page after submission
            // window.location.href = '/thank_you'; // Redirect to thank you page
        } catch (error) {
            console.error('Error submitting application:', error);
            alert('Failed to submit application. Please try again later.');
        }
    });
});
