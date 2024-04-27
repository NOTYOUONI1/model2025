<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Jersey+20+Charted&display=swap" rel="stylesheet">
    <title>Document</title>
</head>
<body>
    <style>
        * {
            margin: 0;
            padding: 0;
            font-family: "Jersey 20 Charted", sans-serif;
            font-weight: 500;
            font-style: normal;
            font-size:30px;
        }
        .main_back{
            height:100%;
            width:100%;
            background:linear-gradient(45deg,#08001f,#30197d);
            display: flex;
            justify-content: center;
        }
        .main{
            height:100vh;
            width:77vw;
            background:linear-gradient(45deg,#0b0326,#300ea1);
            box-shadow: 10px 0 10px -5px rgba(0, 0, 0, 0.5), -10px 0 10px -5px rgba(0, 0, 0, 0.5);
        }
        #nav1{
            height: 5vh;
            background-color: #0b0326;
            display: flex;
            align-items: center;
            justify-content: center;
            color:#2e108f;
        }
        #logo{
            height: 80%;
            border-radius: 50%;
            margin-right: 10px;
        }
        .vav2{
            height: 3vh;
            background-color: #160351;
            display: flex;
            justify-content:center;
            align-items: center;
        }
        a div{
            font-size:20px;
            color:#6139e7;
        }
        a div{
            display: flex;
            align-items: center;
            justify-content: center;
            height: 90%;
            background-color:#2c07a3;
            width: 120%;
            border-radius: 3px;
        }
        a div:hover{
            background-color: #6139e7;
            color: #0b0326;
        }
        .content{
            height: 92vh;
            background:transparent;
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
        }
        .content img{
            height: 20%;
            border-radius: 10px;
            margin: 6%;
        }
    </style>
    <div class="main_back">
        <div class="main">
            <nav id="nav1">
                <img src="https://i1.sndcdn.com/artworks-pmblTZxqAGYOBOCu-TpPOEw-t500x500.jpg" id="logo">
                <h1 id="logoName">O N I</h1>
            </nav>
            <nav class="vav2">
                <a href="/Project">
                    <div>PROJECT</div>
                </a>
            </nav>
            <div class="content">
                <img src="https://i.postimg.cc/hhXWRZhj/61-Zx0-IUiv-HL-UXNa-N-FMjpg-QL85-removebg-preview.png" >
                <img src="https://i.postimg.cc/75MM94XZ/main-qimg-cbe23811ab4316140b865772314d396a-removebg-preview.png" >
                <img src='https://i.postimg.cc/Z9sNs5N4/Jack-Hanma8282.webp' >
            </div>
        </div>
    </div>
</body>
</html>
