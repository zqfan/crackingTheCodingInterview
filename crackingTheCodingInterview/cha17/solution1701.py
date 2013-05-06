"""
Explain what happens, step by step, after you type a URL into a
browser. Use as much detail as possible.

type a url in domain name has some additional steps to type ip address

* check local hosts file to get ip addr of domain name
* if couldn't, contact dns-nameserver to get ip addr
* dns return the ip addr of domain name
* establish a tcp connection to host at port (default may be 80)
* host transfer page code to your client
* browser render the page code
* according to the policy, your browser may disconnect to host after
page code is downloaded, or after you close the tab/window

* dns-nameserver may not find the domain name's ip addr, it will ask
other dns to get the ip addr
* a tcp connection need 3 time3 handshake
* you may use proxy while you're connecting to the host
"""
