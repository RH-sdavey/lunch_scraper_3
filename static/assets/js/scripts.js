function myFunction() {
    var input, filter, cards, cardContainer, h5, keep_card, card_titles, badge_texts, i, j;

    input = document.getElementById("myFilter");
    filter = input.value.toUpperCase();
    cardContainer = document.getElementById("restaurant_cards");
    cards = cardContainer.getElementsByClassName("card");
    for (i = 0; i < cards.length; i++) {
        //We will switch keep_card to true if we find search text in badge or title
        keep_card = false;
        //querySelectorAll returns all elements of a.badge. querySelector returns only the first element
        card_titles = cards[i].querySelectorAll(".card-body h2.card-title");
        badge_texts = cards[i].querySelectorAll(".card-footer i.badge");

        //You must loop through all card titles.
        for(j = 0; j < card_titles.length; j++) {
            if (card_titles[j].innerText.toUpperCase().indexOf(filter) > -1) {
                //Found search text, now lets switch keep_card on
                keep_card = true;
                break;
            }
        }


        if(keep_card) {
            cards[i].style.display = "";
        } else {
            cards[i].style.display = "none";
        }

    }
}