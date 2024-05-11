<h1> A <span style="color:#1D63ED";>Docker Dashboard</span> built in the HackVerse Hackathon </h1>
<h2> Team Name: <span style="color:#ff4747";>Tech Army</span> </h2>

<h2> Features </h2>
<ul>
  <li> Docker Dashboard </li>
  <li> Docker Image Manager </li>
  <li> Docker Container Management </li>
  <li> Docker Chatbot (Exclusively Response only to docker related questions)</li>
  <li> <span style="color:teal;">Bonus </span>:  A Software Engineering bot that responses only to software related queries (Both leverage OpenAI's API) </li>
</ul>

<div>
    <h2> Tech Stack : </h2>
    <ul style="list-style-type: none; display:flex;justify-content: space-evenly;align-items:center;">
        <li style=""> <img src="https://user-images.githubusercontent.com/7164864/217935870-c0bc60a3-6fc0-4047-b011-7b4c59488c91.png" alt="Streamlit logo" style="width:50px"></img></li>
        <li> <img  src="https://avatars.githubusercontent.com/u/1525981?s=200&v=4" style="width:50px"alt="Python"/></li>
        <li style="font-size: 32px;"> 🦜️🔗 </li>
        <li> <img src="https://avatars.githubusercontent.com/u/14957082?s=200&v=4" style="width:50px" alt="OpenAI"/></li>   
        <li> <img src="https://avatars.githubusercontent.com/u/5429470?s=200&v=4" style="width:60px" alt="Docker"/></li>   
    </ul>
</div>

<div>
    <h2> Snapshots </h2>
    <img src="./store/landing1.png" alt="Landing Page"/>
    <img src="./store/landing2.png" alt="Landing Page 2"/>
    <img src="./store/gpt.png" alt="Software GPT"/>
</div>

<div>
    <h2> How to run </h2>
    <ul style="list-style-type: none;">
        <li> Clone the repository </li>
        <li> Create a virtual environment </li>
        <li> Run the following command to install the dependencies </li>
        <code> pip install -r requirements.txt </code>
        <li> Load your environment variables [2 OpenAI api Keys; one for each bot] </li>
        <li> Run the following command to start the server </li>
        <code> streamlit run main.py </code>
    </ul>
</div>

> Note:
> Given that this project is built to access the docker daemon on your computer and run commands, it is recommended to run this project on your local machine.
> That is why we did not deploy this application on the internet. Else we would have to either run it on the daemon of the remote server (security concerns arise) or **Docker-In-Docker**.And that is exactly what we have done here!

<div>
    <h2> Contributors </h2>
    <ul style="list-style-type: none;">
        <li> <a href=""> Disha <span style="color:red";>(Team Lead)</span> </a> </li>
        <li> <a href=""> Swetank <span style="color:#1D63ED";></span> </a> </li>
        <li> <a href=""> Harsh <span style="color:#1D63ED";></span> </a></li>
        <li> <a href=""> Kelmith<span style="color:#1D63ED";></span> </a></li>
</div>
