<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Collect form data
    $name = htmlspecialchars(trim($_POST['name']));
    $email = htmlspecialchars(trim($_POST['email']));
    $message = htmlspecialchars(trim($_POST['message']));

    // Email settings
    $to = "gavinjohnreid@gmail.com"; // Replace with your email
    $subject = "New message from: " . $name;
    $headers = "From: " . $email . "\r\n" .
               "Reply-To: " . $email . "\r\n" .
               "X-Mailer: PHP/" . phpversion();

    // Message content
    $body = "Name: " . $name . "\n" .
            "Email: " . $email . "\n\n" .
            "Message:\n" . $message;

    // Send the email
    if (mail($to, $subject, $body, $headers)) {
        echo "Thank you! Your message has been sent.";
    } else {
        echo "Sorry, there was an issue sending your message. Please try again later.";
    }
}
?>
