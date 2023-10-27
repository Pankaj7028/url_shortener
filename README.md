<b>URL SHORTNER<b>

The project is a basic URL shortener web application built with Python and Flask, a micro web framework. 
|
|
<img src = "https://github.com/Pankaj7028/url_shortener/blob/main/URL_Shortner_Video.gif" width = "800px" />

It offers a simple web interface for users to shorten long URLs and search for existing URLs based on title keywords. The project consists of the following components:

1. **Shortening URLs:** Users can enter a long URL, optionally provide a title, and the application generates a short URL for them. The generated short URLs are stored in a data structure for future access.

2. **Searching URLs:** Users can search for URLs using keywords from the title. The application returns a list of URLs matching the search term along with their titles and short URLs.

3. **Redirecting:** When users access a short URL, the application redirects them to the original long URL. It also tracks the hit count for each short URL.

4. **Web Interface:** The project provides a basic web interface for users to interact with the URL shortener service, where they can submit long URLs for shortening and search for URLs.

This is a simple implementation of a URL shortener service suitable for development and testing. For production use, additional features, security measures, and a more robust storage mechanism may be necessary.
