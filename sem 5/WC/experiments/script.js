function greetUser() {
    alert('Welcome to my webpage!Lets checkout the most wholesome group of whole college');
  }
//   greetUser();


 function validateEmail() {
      const emailInput = document.getElementById('email');
      const email = emailInput.value;
  
      const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!emailPattern.test(email)) {
        alert('Please enter a valid email address.');
        return;
      }
  
      alert('Email is valid: ' + email);
    }

    document.addEventListener('DOMContentLoaded', () => {
        const interests = ['Programming', 'Web Development', 'Reading', 'Hiking'];
        const interestsList = document.getElementById('interestsList');
        const interestInput = document.getElementById('interestInput');
        const addInterestButton = document.getElementById('addInterestButton');
        const currentDateElement = document.getElementById('currentDate');
        const currentTimeElement = document.getElementById('currentTime');
        const additionalInfoElement = document.getElementById('additionalInfo');
      
        displayInterests();
      
        if (addInterestButton && interestInput) {
          addInterestButton.addEventListener('click', () => {
            const newInterest = interestInput.value.trim();
            if (newInterest) {
              interests.push(newInterest);
              displayInterests();
              interestInput.value = '';
            }
          });
        } else {
          console.error('Elements not found.');
        }
      
        function displayInterests() {
          if (interestsList) {
            interestsList.innerHTML = '';  // Clear previous content
            interests.forEach(interest => {
              const listItem = document.createElement('li');
              listItem.textContent = interest;
              interestsList.appendChild(listItem);
            });
          }
        }
      
        const currentDate = new Date();
        const optionsDate = { year: 'numeric', month: 'long', day: 'numeric' };
        const formattedDate = currentDate.toLocaleDateString('en-US', optionsDate);
      
        const currentTime = new Date();
        const optionsTime = { hour: '2-digit', minute: '2-digit', second: '2-digit', timeZoneName: 'short' };
        const formattedTime = currentTime.toLocaleTimeString('en-US', optionsTime);
      
        if (currentDateElement) {
          currentDateElement.textContent = 'Today is ' + formattedDate;
        } else {
          console.error('Element with ID "currentDate" not found.');
        }
      
        if (currentTimeElement) {
          currentTimeElement.textContent = 'Current time is ' + formattedTime;
        } else {
          console.error('Element with ID "currentTime" not found.');
        }
      
        if (additionalInfoElement) {
          additionalInfoElement.textContent = 'YEAH HERE TO NEW ERA OF FUN';
        } else {
          console.error('Element with ID "additionalInfo" not found.');
        }
      });
      


