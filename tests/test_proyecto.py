
from bs4 import BeautifulSoup

def test_extraccion_de_libros():
    html = """
    <article class="product_pod">
        <h3>
            <a title="Libro de prueba">Libro</a>
        </h3>
        <p class="price_color">£25.00</p>
    </article>
    """

    soup = BeautifulSoup(html, "html.parser")

    libro = soup.select_one("article.product_pod")
    nombre = libro.select_one("h3 a")["title"]
    precio = libro.select_one(".price_color").text

    assert nombre == "Libro de prueba"
    assert precio == "£25.00"

