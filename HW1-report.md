# HW1 - Web Science Intro
### Nick Kooshki
### CS 432, Spring 2025
### 2/7/2025

# Q1

The "bow-tie" structure of the web segments the web into several components:
* SCC (Strongly Connected Component): A central core where each node is reachable from any other node within this component.
* IN: Nodes that can reach the SCC but are not reachable from it.
* OUT: Nodes that are reachable from the SCC but cannot reach it.
* Tendrils: Nodes that are connected to either IN or OUT but are not part of the SCC, IN, or OUT.
* Tubes: Nodes that provide direct connections between IN and OUT without passing through the SCC.
* Disconnected: Nodes that are not connected to the SCC, IN, or OUT in any way.

Given the directed links, the graph consists of the following nodes: A, B, C, D, E, F, G, H, I, J, K, L, M, N, O.
* SCC:
- Nodes: A, B, C, D, G
- These nodes form a cycle where each node is reachable from any other node within this set.
* IN:
- Nodes: M
- Node M can reach the SCC (via A) but is not reachable from the SCC.
* OUT:
- Nodes: H, L
- Nodes H and L are reachable from the SCC (via D → H → L) but do not link back to the SCC.
* Tendrils:
- From IN:
- Nodes: None
- There are no nodes that are reachable from M (IN) that are not part of the SCC or OUT.
- To OUT:
- Nodes: None
- There are no nodes that can reach H or L (OUT) that are not part of the SCC or IN.
* Tubes:
- Nodes: None
- There are no nodes that provide a direct connection from IN to OUT without passing through the SCC.
* Disconnected:
- Nodes: E, F, I, J, K, N, O
- These nodes are not connected to the SCC, IN, or OUT components.

# Q2

* Part A: The "User-Agent" header

[Screenshot 1](hw1-q2ss1.png)

Loading the webpage in your browser displays the User-Agent string that your browser sends by default, which typically includes details like the browser name, version, and operating system.

* Part B: The curl command requesting the URI with specific options

[Screenshot 2](hw1-q2ss2.png)

Executing the curl command with options to show HTTP response headers, follow redirects, and set the User-Agent to "CS432/532" results in the display of the HTTP headers from the final destination. However, since the -I option is used, only headers are shown, and the response body (which would echo the User-Agent) is not included.

* Part C: The curl command requesting the URI, saving the HTML output to a file

[Screenshot 3](hw1-q2ss3.png)

Running the curl command with options to follow redirects, set the User-Agent to "CS432/532", and save the output to output.html stores the HTML content of the response in the specified file. This file contains the echoed User-Agent string, confirming that the server received the custom User-Agent header.

* Part D: Viewing the HTML output file

[Screenshot 4](hw1-q2ss4.png)

Opening output.html in a web browser displays the content of the file, which shows the User-Agent string "CS432/532", verifying that the server processed and echoed back the custom User-Agent header sent in the request.

# Q3

[Link to Python file](collect-webpages.py)

[URIs list](collected_uris.txt)

I used the method of starting with an initial seed webpage and extracting all valid HTML links from it. For each extracted link, I checked whether it was an HTML page with more than 1000 bytes of content. If it met the criteria, I added it to the list of collected URIs. To gather 500 unique URIs, I used a recursive approach where the program selected the last collected valid URI as the new seed and repeated the process until the required count was reached.

* Some examples of seed webpages that were used in the list:

- https://weiglemc.github.io/
- https://arxiv.org/
- https://www.odu.edu/
- https://www.slideshare.net/
- https://www.linkedin.com/

# References

* ChatGPT task, question 1: <https://chatgpt.com/share/67a692b6-7830-800f-bce0-17747cbd6562>

* ChatGPT task, question 2: <https://chatgpt.com/share/67a69f08-e76c-800f-9b8a-0f07c171c26a>

* ChatGPT task, question 3: <https://chatgpt.com/share/67a6af1f-1168-800f-b220-2dbfdcf8eff4>