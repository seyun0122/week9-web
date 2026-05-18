from bootstrap.container import Container
import os

def main():
    app = Container().build_app()

    port = int(os.environ.get("PORT", 7860))

    print("==== DEBUG START ====")
    print("PORT =", port)
    print("APP TYPE =", type(app))
    print("APP =", app)
    print("==== DEBUG END ====")

    app.launch(
        server_name="0.0.0.0",
        server_port=port,
        share=False
    )

if __name__ == "__main__":
    main()
