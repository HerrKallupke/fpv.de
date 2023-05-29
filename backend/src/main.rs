use tokio_postgres::types::ToSql;
use tokio_postgres::Client;
use warp::{Filter, Reply};
use serde_json::{json, Value};
use std::sync::Arc;

mod db;

#[ tokio::main ]
async fn main() {
    println!("Connection to database...");

    let db_connection_result  = db::connect("localhost", "5678", "postgres", "test", "postgres").await;

    match db_connection_result {
        Ok(client) => {
            println!("Successfully connected to database.");

            run_api(client).await;
        }

        Err(error) => {
            eprint!("Database connection error: {}", error);
        }
    }
}

async fn run_api(client: Client){
    let client = Arc::new(client);

    let search = warp::path!("search" / String).and_then({
        move | query | search(query, client.clone())
    });

    warp::serve(search).run(([127, 0, 0, 1], 3030)).await;
}

async fn search(query: String, client: Arc<Client>) -> Result<impl Reply, warp::Rejection> {
    let search_result = client.query("SELECT * FROM flyingfolk WHERE title LIKE $1", &[&format!("{}%", query)]).await;

    match search_result {
        Ok(rows) => {
            if rows.len() > 0 {
                let mut titles: Vec<String> = Vec::new();

                for row in rows {
                    titles.push(row.get("title"));
                }

                let json = json!(titles);

                Ok(warp::reply::json(&json))
            }else {
                Ok(warp::reply::json::<String>(&"No results".to_string()))
            }
        }
        Err(error) => {
            Ok(warp::reply::json(&format!("Database error: {}", error)))
        }
    }
}