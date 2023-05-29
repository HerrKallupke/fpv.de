use tokio_postgres::{ Client, NoTls, Error };

pub async fn connect(host: &str, port: &str, user: &str, password: &str, name: &str) -> Result<Client, Error> {
    let (client, connection) = tokio_postgres::connect(&format!("host={} port={} user={} password={} dbname={}", host, port, user, password, name), NoTls).await?;

    tokio::spawn(async move {
        if let Err(e) = connection.await {
            eprint!("Database error: {}", e);
        }
    });

    Ok(client)
}