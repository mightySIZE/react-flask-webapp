from MSapp import app

# this line will run the app, will run only if module is directly run and not as an import from another module
if __name__ == '__main__':
    print("I am being run directly")
    app.run(debug=True)