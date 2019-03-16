let font;
let awanImg;
let bg;
let awan = [];
let awanLen = 3;

function preload() {
  font = loadFont("/static/assets/font/FredokaOne.ttf");
  awanImg = loadImage("/static/assets/img/awan.png");
  bg = loadImage("/static/assets/img/bg.png");
}

function setup() {
  createCanvas(windowWidth, windowHeight);

  for (let i = 0; i < awanLen; i++) {
    awan[i] = new Awan(width + random(300), random(height - 200));
  }
}

function draw() {
  background(255, 240, 240);
  background(bg, 0, windowHeight - bg.height);

  fill(250, 190, 190);
  noStroke();
  textSize(130);
  textAlign(CENTER);
  textFont(font);
  text("404", width / 2, height / 2 - 100);

  textSize(40)
  text("Maap, Halaman Tidak Tersedia", width / 2, height / 2);

  for (let i = 0; i < awan.length; i++) {
    awan[i].tampilkan();
    awan[i].gerak();
    if (awan[i].cekTepi()) {
      awan.splice(i, 1);
      awan.push(new Awan(width + random(100), random(height - 200)));
    }
  }
}

class Awan {
  constructor(x, y) {
    this.pos = createVector(x, y);
    this.step = random(0.3, 0.9);
  }

  tampilkan() {
    image(awanImg, this.pos.x, this.pos.y);
  }

  gerak() {
    this.pos.x -= this.step;
  }

  cekTepi() {
    if (this.pos.x < -awanImg.width) {
      return true;
    }
  }
}