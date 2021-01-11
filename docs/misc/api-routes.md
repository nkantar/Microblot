# Internal API Routes

These routes are intended for the Netlify builder to use to fetch data.
Some day they may power some external API.

| Route | Description |
|:----- |:----------- |
| `GET /blogs` | all blogs |
| `GET /blogs/<blog_id>` | blog metadata |
| `GET /blogs/<blog_id>/posts` | all posts for given blog |
| `GET /blogs/<blog_id>/authors` | all authors for given blog |
| `GET /blogs/<blog_id>/authors/<author_id>` | author metadata |
| `GET /blogs/<blog_id>/authors/<author_id>/posts` | all posts for given author |
| `GET /categories` | all categories |
| `GET /categories/<category_id>` | category metadata |
| `GET /categories/<category_id>/posts` | all posts for given category |
