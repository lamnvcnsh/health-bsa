# Health-BSA
A small tool to estimate the human body surface area (BSA) from body weight (kg) and height (cm).
This tool supports 5 methods

- Du Bois 
- Mosteller
- Haycock
- Gehan and George
- Fujimoto

More information about those method can be found [here](https://www.tandfonline.com/doi/abs/10.1080/03014460801908439?journalCode=iahb20)
### Getting started

The package can be found in the pip.

```bash
pip install health-bsa
```

### Usage

This function required two main information:
- Body weight (kg)
- Body height (cm)

```python
>>> from health_bsa import BSA
>>> BSA(weight=60,height=170)
```

The default method is **Du Bois**, if you would like to use another method using **Method** argument.


```python
>>> from health_bsa import BSA
>>> BSA(weight=60,height=100, method="Mosteller")
```
You might want to change number of digits, you can use digits parameter.

```python
>>> from health_bsa import BSA
>>> BSA(weight=60,height=100, digits=3)
```


### Contribution
Any contributions are welcome.

### Author
Lam Nguyen