SELECT sc.`id_sucursal`, sucursal.`nombre_encargado`, CONCAT( contactos.`identificacion`, contactos.`nom_representante`), sucursal.`id_pais`
FROM sucursal_cliente sc
INNER JOIN sucursal ON sucursal.`id` = sc.`id_sucursal`
INNER JOIN contactos ON contactos.`id` = sc.`id_contacto`
GROUP BY sc.`id_sucursal`
