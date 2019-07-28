from flask import Flask, render_template, request, jsonify
from addons import 	NhacCuaTui, ZingMp3
app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html", title = "NoCSS")

@app.route("/music")
def music():
	id = request.args.get("id")
	ispl = True if request.args.get("ispl") == "true" else False

	nct = NhacCuaTui.NCT(id, ispl)

	return nct.link_mp3
if __name__ == "__main__":
	app.run(debug=True)