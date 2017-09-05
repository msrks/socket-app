# socket apps

for Network Test using RPI

## Requirements

timeout_decorator

- ubuntu, raspbian

```
$ sudo apt-get install python-pip
$ sudo pip install timeout_decorator
```

- mac

```
(pyenv)$ pip install timeout_decorator
```

## Usage

- parent_bc.py

```
$ python parent_bc.py <dst-ip> <num-child> <interval>
$ python parent_bc.py 192.168.88.255 16 0.1
```

- parent_bc_exact_polling.py

```
$ python parent_bc_exact_polling.py <dst-ip> <num-child> <interval>
$ python parent_bc_exact_polling.py 192.168.88.255 16 0.1
```

- parent_uc.py

```
$ python parent_uc.py <dst-ip> <src-port> <interval>
$ python parent_uc.py 192.168.88.102 30003 0.1
```

- child.py

```
$ python child.py
```
