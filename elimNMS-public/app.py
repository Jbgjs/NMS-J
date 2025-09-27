from elimNMS.server import server as app # noqa: F401

if __name__ == "__main__":
    print("Starting elimNMS server...")
    print("Access the web interface at: http://localhost:5000")
    print("Press Ctrl+C to stop the server")
    app.run(host='0.0.0.0', port=5000, debug=False)