Ejercicio 1:

En este ejercicio me pedian una api que pudiera aceptar el numero de cliente y devolviera
```
{
    "Resultado":  [
        {
            "NroCliente": x,
            "Score": yyy,
            "Score_50": zzz        
        }
    ]
}
```

Lo que hice fue crear una simple Flask App. 

Con el decorador route hice que el endpoint acepte variables que fueran solo enteros.

Luego con Pandas leo el archivo CSV.xltx

Filtro el dataframe para quedarme con la fila que tenga el numero del cliente solicitado.

Chequeo si esta vacio, en ese caso de lo que este responde con resultado vacio:
```
{
    "Resultado":  []
}
```
Para calcular score_50 divido score por 50 y uso math.floor para redondear hacia abajo hasta el proximo entero y luego multiplico por 50.

Como int64 y float64 no me eran aceptados por el encoding por defecto para pasar a json tengo que convertir los resultados de
la query a int y float segun corresponda.

Para levantar la api correr dentro de la carpeta ClientAPI
```
flask --app App run
```
y el link deberi ser http://127.0.0.1:5000/<NroCliente>

Las librerias necesarias para correr este ejercicio son:
* openpyxl
* pandas
* Flask

Ejercicio 2:

```
SELECT count(*)
FROM (
    SELECT * FROM CONSULTAS
    WHERE
        CUIT_Consultado = "CUIT A CONSULTAR" and
        FechaHora > DATETIME("now", "-30 day")
    ) CONSULTAS
JOIN (
    SELECT * FROM TIPO_CONSULTAS
    WHERE
        DescripcionTipoConsulta in ("Nosis Manager","Nosis VID")
    ) TIPO_CONSULTAS
ON CONSULTAS.IdTipoConsulta=TIPO_CONSULTAS.IdTipoConsulta
JOIN (
    EMPRESAS
    JOIN 
    BANCOS ON EMPRESAS.CUIT_Empresa=BANCOS.CUIT_bancos
    ) EMPRESAS 
ON CONSULTAS.IdEmpresa=EMPRESAS.IdEmpresa
```

En este ejercicio me piden contar la cantidad de veces que bancos consultaron un cuit en 
particular con tipo de consulta Nosis Manager o Nosis VID en los ultimos 30 dias.

1) Empiezo con un select count(*) porque solo me importa el numero de casos de mi query
2) Segundo la tabla de consultas filtro las consultas que sean del cuit consultado y que sean consultas
de hace menos de 30 dias de hoy
3) Voy a juntar el anterior resultado con la tabla TIPO_CONSULTAS, pero de esta solo me quedo con las consultas tipo Nosis Manager o Nosis VID
4) Cuando junto las 2 tablas anteriores las junto en las columnas IdTipoConsulta 
5) Luego necesito quedarme con las consultas de los bancos, para esto junto las tablas EMPRESAS y BANCOS en la columna CUIT_EMPRESAS con CUIT_BANCOS
6) Finalmente hago un JOIN con el resultado de 5) con lo anterior en IdEmpresa.