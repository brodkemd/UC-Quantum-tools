def Image(path:str):
    #path = path.replace("#", "%23")
    #return f"<div class=\"myZoomist\" data-zoomist-src=\"{{URI}}{path}\"></div>"
    return f"<img src=\"{{URI}}{path}\" alt=\"no image to display\">"