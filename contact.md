---
layout: page
title: Contact
permalink: /contact/
---

# Get in Touch

Have a question about a recipe, need help troubleshooting your bread, or want to suggest a tool review? I'd love to hear from you!

<form action="https://formspree.io/f/{{ site.formspree_form_id }}" method="POST" class="contact-form">
  <div class="form-group">
    <label for="name">Name</label>
    <input type="text" id="name" name="name" required>
  </div>

  <div class="form-group">
    <label for="email">Email</label>
    <input type="email" id="email" name="_replyto" required>
  </div>

  <div class="form-group">
    <label for="subject">Subject</label>
    <select id="subject" name="subject" required>
      <option value="" disabled selected>What can I help you with?</option>
      <option value="general">General Inquiry</option>
      <option value="recipe-question">Recipe Question</option>
      <option value="tool-suggestion">Tool Review Request</option>
      <option value="troubleshooting">Troubleshooting Help</option>
    </select>
  </div>

  <div class="form-group urgent-checkbox">
    <label for="urgent" class="urgent-label">
      <input type="checkbox" id="urgent" name="urgent" value="yes" onchange="updateSubject()" class="urgent-input">
      <span class="urgent-text">🚨 Mark as URGENT (dough currently misbehaving!)</span>
    </label>
  </div>

  <div class="form-group">
    <label for="message">Message</label>
    <textarea id="message" name="message" rows="6" required placeholder="What's on your mind?"></textarea>
  </div>

  <!-- Formspree honeypot field for spam protection -->
  <input type="text" name="_gotcha" style="display:none">

  <!-- Hidden field to set the subject line in emails -->
  <input type="hidden" id="subject-field" name="_subject" value="New contact form submission from Dough Main Logic">

  <!-- Prevent redirect - return JSON response instead -->
  <input type="hidden" name="_format" value="json">

  <script>
    function updateSubject() {
      const urgentCheckbox = document.getElementById('urgent');
      const subjectField = document.getElementById('subject-field');
      const baseSubject = 'New contact form submission from Dough Main Logic';

      if (urgentCheckbox.checked) {
        subjectField.value = 'URGENT - ' + baseSubject;
      } else {
        subjectField.value = baseSubject;
      }
    }

    // Handle form submission with AJAX
    document.addEventListener('DOMContentLoaded', function() {
      const form = document.querySelector('.contact-form');
      const submitBtn = document.querySelector('.submit-btn');

      form.addEventListener('submit', function(e) {
        e.preventDefault();

        // Disable submit button and show loading
        submitBtn.disabled = true;
        submitBtn.textContent = 'Sending...';

        // Submit form data via fetch
        fetch(form.action, {
          method: 'POST',
          body: new FormData(form),
          headers: {
            'Accept': 'application/json'
          }
        }).then(response => {
          if (response.ok) {
            // Success - show popup and clear form
            showThankYouPopup();
            form.reset();
            document.getElementById('subject-field').value = 'New contact form submission from Dough Main Logic';
          } else {
            throw new Error('Form submission failed');
          }
        }).catch(error => {
          alert('Sorry, there was an error sending your message. Please try again.');
        }).finally(() => {
          // Re-enable submit button
          submitBtn.disabled = false;
          submitBtn.textContent = 'Send Message';
        });
      });
    });

    function showThankYouPopup() {
      // Create popup overlay
      const overlay = document.createElement('div');
      overlay.style.cssText = `
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0, 0, 0, 0.5);
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 1000;
        padding: 1rem;
        box-sizing: border-box;
      `;

      // Create popup content
      const popup = document.createElement('div');

      // Check if mobile device
      const isMobile = window.innerWidth <= 768;

      popup.style.cssText = `
        background: white;
        padding: ${isMobile ? '1.5rem' : '2rem'};
        border-radius: ${isMobile ? '12px' : '15px'};
        max-width: ${isMobile ? '90vw' : '400px'};
        width: 100%;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
        max-height: 90vh;
        overflow-y: auto;
      `;

      popup.innerHTML = `
        <h3 style="color: #8B4513; margin-bottom: 1rem; font-size: ${isMobile ? '1.3rem' : '1.5rem'};">
          Message Sent! 🍞
        </h3>
        <p style="margin-bottom: 1.5rem; line-height: 1.5; font-size: ${isMobile ? '0.95rem' : '1rem'};">
          Thanks for reaching out! I typically respond within 24-48 hours.
          If you marked your message as urgent, I'll prioritize it.
        </p>
        <button onclick="this.parentElement.parentElement.remove()"
                style="background: #8B4513; color: white; border: none;
                       padding: ${isMobile ? '1rem 2rem' : '0.75rem 1.5rem'};
                       border-radius: ${isMobile ? '12px' : '8px'};
                       cursor: pointer; font-weight: 600;
                       font-size: ${isMobile ? '1.1rem' : '1rem'};
                       min-height: ${isMobile ? '48px' : 'auto'};
                       width: ${isMobile ? '100%' : 'auto'};
                       touch-action: manipulation;">
          Close
        </button>
      `;

      // Add click outside to close
      overlay.addEventListener('click', function(e) {
        if (e.target === overlay) {
          overlay.remove();
        }
      });

      // Add escape key to close
      const escapeHandler = function(e) {
        if (e.key === 'Escape') {
          overlay.remove();
          document.removeEventListener('keydown', escapeHandler);
        }
      };
      document.addEventListener('keydown', escapeHandler);

      overlay.appendChild(popup);
      document.body.appendChild(overlay);

      // Auto-close after 7 seconds
      setTimeout(() => {
        if (overlay.parentElement) {
          overlay.remove();
          document.removeEventListener('keydown', escapeHandler);
        }
      }, 7000);
    }
  </script>

  <button type="submit" class="submit-btn">Send Message</button>
</form>
