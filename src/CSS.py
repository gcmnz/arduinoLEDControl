
FONT_STYLE = """<font style='
        color: rgba(210, 210, 210, 255);
        font-weight: 611;
        font-family: Comic Sans MS;
        font-size: 22px;'>"""

CSS_STYLES = """
    MainWindow {
        background-color: rgba(15,  15,  15, 255);
    }
    
    QLabel {
        padding: 10px;
    }

    QPushButton {
        font-weight: 611;
        font-style: italic;
        font-family: Comic Sans MS;
        font-size: 24px;
        
        background-color: rgba(255, 255, 255, 255);
        
        min-height: 40px;
        margin: 0px 100px 0px 100px;

        border-radius: 20px;
    }

    QPushButton::hover {
        background-color: rgba(200, 200, 200, 255);
    }

    QPushButton::pressed {
        background-color: rgba(180, 180, 180, 255);
    }
    
    QSlider::groove:horizontal {
        border: 1px solid #bbb;
        background: white;
        height: 10px;
        border-radius: 4px;
    }
    
    QSlider::sub-page:horizontal {
        background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #000, stop: 1 #bbb);
        border: 1px solid #777;
        height: 10px;
        border-radius: 4px;
    }
    
    QSlider::add-page:horizontal {
        background: rgba(200, 200, 200, 255);
        border: 1px solid #777;
        height: 10px;
        border-radius: 4px;
    }
    
    QSlider::handle:horizontal {
        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #eee, stop:1 #fff);
        border: 1px solid #000;
        width: 14px;
        margin-top: -5px;
        margin-bottom: -5px;
        border-radius: 4px;
    }
    
    QSlider::handle:horizontal:hover {
        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #fff, stop:1 #ddd);
        border: 1px solid #444;
        border-radius: 4px;
    }
    

"""
