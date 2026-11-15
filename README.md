# Machine Learning Web Application

A Flask-based web application that serves predictions from a trained `scikit-learn` machine learning model[span_0](start_span)[span_0](end_span).

## Features
- Interactive web interface served via Flask[span_1](start_span)[span_1](end_span).
- Real-time predictions via the `/predict` POST endpoint[span_2](start_span)[span_2](end_span).
- Progressive Web App (PWA) ready with `manifest.json` and app icons[span_3](start_span)[span_3](end_span).
- Production-ready setup using `gunicorn`[span_4](start_span)[span_4](end_span).

## Tech Stack
- **Backend:** Python 3.13, Flask 3.1.2, Gunicorn 27.0.1[span_5](start_span)[span_5](end_span)
- **Machine Learning & Data:** scikit-learn 1.7.2, NumPy 2.3.5, SciPy 1.16.3[span_6](start_span)[span_6](end_span)

## Project Structure
```text
├── app.py                 # Main Flask application and prediction routes
├── requirements.txt       # Python dependencies
├── static/                # Static assets (CSS, JS, manifest.json, icons)
└── templates/             # HTML templates
