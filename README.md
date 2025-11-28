**Simple example of the password protected website**<br>
i made it in free time ^-^

**How it work?**<br>
consisting of 2 static html, index.html and login html, with Fastapi backend using python<br>
upon accesing the web the backend check wether u had logged in or not, in this case no, it will FileResponse to login.html<br>
Login page consist of simple html no advanced js needed, it use a form which consist of input,to enter the password, and button, to sumbit, using POST method to reach the backend and check whether the password stored in backend match the password from the form.<br>
if enetered correctly it will FileResponse to index.html,with a logout button if u wanna try again.

**Question**<br>
can ppl bypass it by redirecting to index.html?<br>
ans: no as the only way to get index.html is via the fileresponse from backend.

**How could I improve it?**<br>
Ovbiously the ui or maybe the entire code and structure as i am not a full expert toward this stuff, but i will learn no matter what.
