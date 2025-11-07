import logging

logger = logging.getLogger(__name__)    
table = "yt_api"

def insert_rows(cur, conn, schema,row):
    try:

        if schema == 'staging':
            video_id = 'video_id'
            
            cur.execute(f"""INSERT INTO {schema}.{table}
                ('Video_ID','Video_Title','Upload_Date','Duration','Video_Views','Likes_Count','Comments_Count')
                    VALUES 
                (%(video_id)s, %(title)s, %(published_at)s, %(duration)s, %(view_count)s, %(like_count)s, %(comment_count)s); 
                    """, row)
            
            conn.commit()
            logger.info("Successfully inserted row into staging table")
        else:
            video_id = 'Video_Id'
            cur.execute(f"""INSERT INTO {schema}.{table}
                ('Video_ID','Video_Title','Upload_Date','Duration','Video_Type','Video_Views','Likes_Count','Comments_Count')
                    VALUES 
                (%(Video_Id)s, %(Video_Title)s, %(Upload_Date)s, %(Duration)s, %(Video_Type)s, %(Video_Views)s, %(like_count)s, %(comment_count)s); 
                    """, row)
            
            conn.commit()
            logger.info(f"Inserted row with Video_ID {row['Video_ID']}")

    except Exception as e:
        logger.error(f"Errorplementation of inserting row into {table}: {e}")
        conn.rollback()

def update_rows(cur,conn,schema,row):
    try:
        if schema == 'staging':
            video_id = 'video_id'
            cur.execute(f"""UPDATE {schema}.{table}
                SET 
                    "Video_Title" = %(title)s,
                    "Upload_Date" = %(published_at)s,
                    "Duration" = %(duration)s,
                    "Video_Views" = %(view_count)s,
                    "Likes_Count" = %(like_count)s,
                    "Comments_Count" = %(comment_count)s
                WHERE "Video_ID" = %(video_id)s;
                    """, row)
            
            conn.commit()
            logger.info(f"Successfully updated row with Video_ID {row['video_id']}")
        else:
            video_id = 'Video_Id'
            cur.execute(f"""UPDATE {schema}.{table}
                SET 
                    "Video_Title" = %(Video_Title)s,
                    "Upload_Date" = %(Upload_Date)s,
                    "Duration" = %(Duration)s,
                    "Video_Type" = %(Video_Type)s,
                    "Video_Views" = %(Video_Views)s,
                    "Likes_Count" = %(like_count)s,
                    "Comments_Count" = %(comment_count)s
                WHERE "Video_ID" = %(Video_Id)s;
                    """, row)
            
            conn.commit()
            logger.info(f"Successfully updated row with Video_ID {row['Video_Id']}")

    except Exception as e:
        logger.error(f"Error updating row in {table}: {e}")
        conn.rollback() 

def delete_rows(cur,conn,schema,ids_to_delete):
    try:
        ids_to_delete = f"""({', '.join(f"'{id}'" for id in ids_to_delete)})"""
        cur.execute(f"""DELETE FROM {schema}.{table}
            WHERE "Video_ID" IN {ids_to_delete};
                """)
        
        conn.commit()
        logger.info(f"Successfully deleted row with Video_ID {ids_to_delete}")

    except Exception as e:
        logger.error(f"Error deleting {ids_to_delete}: {e}")
        conn.rollback()
