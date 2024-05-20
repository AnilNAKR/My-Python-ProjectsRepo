### ISS Tracker with Email Notification

This Python script tracks the International Space Station (ISS) using the ISS API and sends email notifications when the ISS is overhead during the night at a specified location.

## Features

1) **ISS Tracking:** The script retrieves the current latitude and longitude of the ISS using the ISS API and checks if it is within a certain range of a predefined location.

2) **Nighttime Detection:** It determines whether it is nighttime at the specified location by comparing the current time with the sunrise and sunset times obtained from the Sunrise-Sunset API.

3) **Email Notification:** When the ISS is overhead during the night, the script sends an email notification to a specified email address using the SMTP protocol.
