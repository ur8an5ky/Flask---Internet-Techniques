const canvas = document.getElementById("cvs");
const ctx = canvas.getContext("2d");
const pattern = document.getElementById("pattern");

const CH = (canvas.height = 600);
const CW = (canvas.width = 700);

canvas.style.borderLeft = "5px solid black";
canvas.style.borderRight = "5px solid black";
canvas.style.borderTop = "5px solid white";
canvas.style.borderBottom = "5px solid white";

let showBallPath = false;

function showPath() {
  showBallPath = !showBallPath;
}

pattern.addEventListener("onclick", showPath);

const bounceBall = {
  speed: 8,
  velocity_x: 2,
  velocity_y: 2,
  radius: 10,
  color: "rgb(255, 123, 0)",
  angle: 50, // MOŻE EDYTOWALNE????
  position: {
    x: CW / 2,
    y: CH / 2,
  },

  setValues(spee, radi) {
    this.speed = spee;
    this.radius = radi;
    },

  draw() {
    showBallPath ? "" : ctx.clearRect(0, 0, CW, CH); // ?FOR CLEAR PERVIOUS CANVAS
    ctx.fillStyle = this.color;
    ctx.beginPath();
    ctx.arc(this.position.x, this.position.y, this.radius, 0, 2 * Math.PI);
    ctx.closePath();
    ctx.fill();
  },
  update() {
  debugger;
    if (
      this.position.x + this.radius > CW ||
      this.position.x - this.radius < 0
    ) {
       this.angle = 180 - this.angle;
      this.color = "rgb(0, 122, 255)";
   
    }
    if (
      this.position.y + this.radius > CH ||
      this.position.y - this.radius < 0
    ) {
      this.angle = 360 - this.angle;


      this.color = "rgb(255, 123, 0)";
    }

    this.velocity_x = Math.cos(this.angle * (Math.PI / 180)) * this.speed;
    this.velocity_y = Math.sin(this.angle * (Math.PI / 180)) * this.speed;
   console.log(this.velocity_y,this.velocity_x);
    this.position.x += this.velocity_x;
    this.position.y += this.velocity_y;
  },
};

function render(spee, radi) {
  bounceBall.setValues(spee, radi);
  bounceBall.draw();
  bounceBall.update();
}

function gameLoop() {
  let spe = parseInt(document.getElementById("speed").value);
  let rad = parseInt(document.getElementById("radius").value);
  render(spe, rad);

  window.requestAnimationFrame(gameLoop);
}
 window.requestAnimationFrame(gameLoop);

//? YOUR CAN USE SETINTERVAL FUNCTION AS WELL BUT REQUESTANIMATIONFRAME HAS OWN ADVANTAGES
// setInterval(() => {
//   gameLoop();ho
// }, 1000 / 60);
