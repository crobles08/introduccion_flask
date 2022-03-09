SELECT sucursal_cliente.`id_contacto` AS ID_CLIENTE, contactos.`nom_representante` AS NOMBRE_CLIENTE,  COUNT(sucursal_cliente.`id_sucursal`) AS CANTIDAD_SUCURSALES
FROM sucursal_cliente
INNER JOIN contactos ON sucursal_cliente.`id_contacto` = contactos.`id`
GROUP BY sucursal_cliente.`id_contacto`

