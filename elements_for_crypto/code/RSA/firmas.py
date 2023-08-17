from tools_blocks2message import *
from tools_message2blocks import *
from tools_for_RSA import *
import sympy.ntheory as nt

mi_mensaje = 'hola mundo'
print(message2blocks(mi_mensaje, possible_len=2))

p_b, q_b, m_b, e_b = init_keys(10000)
phi_m_b = nt.totient(m_b)
d_b = inverse_of(e_b, phi_m_b)
p_c, q_c, m_c, e_c = init_keys(1000)
phi_m_c = nt.totient(m_c)
d_c = inverse_of(e_c, phi_m_c)

pub_key_c, priv_key_c = (e_c, m_c), (d_c, m_c)
pub_key_b, priv_key_b = (e_b, m_b), (d_b, m_b)

print("clave pública del banco (e_b, m_b): ", pub_key_b)
print("clave privada del banco (d_b, m_b): ", priv_key_b)
print("clave pública del cliente (e_c, m_c): ", pub_key_c)
print("clave privada del cliente: (d_c, m_c) ", priv_key_c)

bs = message2blocks(mi_mensaje, possible_len=2)

mensaje_firmado = encode_rsa(m_b, e_b, decode_rsa(m_c, d_c, bs))
print(mensaje_firmado)

d_mensaje_firmado = encode_rsa(m_c, e_c, (decode_rsa(m_b, d_b, mensaje_firmado)))
print(blocks2message(d_mensaje_firmado))