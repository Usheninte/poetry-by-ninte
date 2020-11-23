# Notes

> [Key Documentation](https://docs.getpelican.com/en/4.5.0/publish.html#make)

If you want to use `make` to generate your site using the settings in `pelicanconf.py`, run:

```
make html
```

To generate the site for production, using the settings in `publishconf.py`, run:

```
make publish
```

If you’d prefer to have Pelican automatically regenerate your site every time a change is detected (which is handy when testing locally), use the following command instead:

```
make regenerate
```

To serve the generated site so it can be previewed in your browser at http://localhost:8000/:

```
make serve
```

Normally you would need to run `make regenerate` and `make serve` in two separate terminal sessions, but you can run both at once via:

```
make devserver
```
