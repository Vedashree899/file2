from flask import Flask, render_template, Response
import cv2
import os
app = Flask(_name)
#load the YOLOv5 model (ensure correct path to the .pt file)
model_path = 'c:/users/admin/Desktop/vedashree/yolov5/yolov5s.pt'
if not os.path.exists(model_path):
  raise FilenotFoundError(f"model file not found at :{model_path}")
  # Load yolov5 model from the provided path
  model = torch.hub.load('ultralytics/yolov5','custom',path=model_path,force_reload=True)bre
  # Function to generate video frames with Yolov5 detection
  def generate_frames():
    camera = cv2.videoCapture(0)
    while True:
      # Read the camera frame
      success, frame = camera .read()
      if not success:
        break
      else:
        # Perform object detection using Yolov5
        result_ing = results.render()[0]
        # Encode the result image as a JPEG format
        ret, buffer = cv2.imencode('.jpg',result_ing)
        frame = buffer.tobytes()
        # Yield the frame in the required formate for streaming
yield (b'--frame\r\n'
       b'content-Type:image/jpeg\r\n\r\n' = frame + b'\r\n')
@app.route('/')
def index():
  # Render the main page template 
  return render_template('index.html')
  @app.route('/video_feed')
  def video_feed():
    # Route to serve the video feed
    return Response(generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')
    if__name__=='main__':
    app.run(debug=True)
        
