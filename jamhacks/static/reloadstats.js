      // Establish a WebSocket connection
      const socket = new WebSocket('wss://example.com/socket');

      // Function to handle data received from the WebSocket
      function handleData(data) {
        // Update the HTML element with the received data
        document.getElementById('data-element').textContent = data;
      }

      // Listen to the WebSocket messages
      socket.addEventListener('message', function(event) {
        // Call the handleData function with the received data
        handleData(event.data);
      });

      // Check WebSocket connection status every second
      setInterval(function() {
        if (socket.readyState !== WebSocket.OPEN) {
          // WebSocket connection is closed or in the process of closing
          // You can handle this situation accordingly (e.g., reconnect)
        }
      }, 1000);