# Django Signals are Evil Incarnate

Code examples for [the presentation on the Django Signals misuses and good steps](https://docs.google.com/presentation/d/1zVyYFS9Pry6WrdRDxwMcOlvdLr2K-r8UPw2DikRkEYQ/edit?usp=sharing) on how to improve our road from monolith to microservices.

Examples are avaiable in the separated branches:
- [Exapmle 1](https://github.com/ivellios/what-is-wrong-with-signals/tree/example1) -- using regular signals `pre_save` and `post_save`
- [Exapmle 2](https://github.com/ivellios/what-is-wrong-with-signals/tree/example2) -- using custom defined signals
- [Exapmle 3](https://github.com/ivellios/what-is-wrong-with-signals/tree/example3) -- adding explicit Message dataclasses and decoupling
- [Exapmle 4](https://github.com/ivellios/what-is-wrong-with-signals/tree/example4) -- celery-based tasks asynchronous processing
