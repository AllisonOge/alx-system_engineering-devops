# Postmortem: NGINX Server Downtime Due to Faulty Production Update



## Issue Summary

- **Duration:**
  - Start Time: April 8, 2024, 09:48 AM (MDT)
  - End Time: April 8, 2024, 07:22 PM (MDT)
- **Impact:**
  - The NGINX server with a replicated SQL database crashed following an unintended code deployment to production.
  - Approximately 65% of users experienced intermittent access and slow response times.
  - Root cause was a faulty code update that disrupted server stability under high load conditions.
- **Root Cause:**
  - A piece of inefficient database query logic was introduced, which increased the load on the database servers beyond sustainable limits during peak traffic.

## Timeline

- **Detection:**
  - The issue was detected immediately through automated monitoring alerts indicating high response times and error rates.

- **Actions Taken:**
  - Initial investigation focused on network and hardware issues.
  - Database logs and recent code deployments were reviewed to identify any abnormal activities.

- **Misleading Paths:**
  - Initial assumptions that the issue was related to network congestion delayed proper identification of the root cause.

- **Escalation:**
  - The issue was escalated to the senior development team and database administrators.

- **Resolution:**
  - The system was restored by reverting to the previous stable version of the production code.

## Root Cause and Resolution

- **Root Cause:**
  - The new code deployment introduced a complex SQL query that lacked proper indexing and caused full table scans under high load, leading to database lockups and server crashes.
- **Resolution:**
  - The faulty deployment was rolled back, and the previous stable version of the code was reinstated. The system returned to normal operational levels following the rollback.

## Corrective and Preventative Measures

- **Improvements/Fixes:**
  - Implementing a more rigorous code review and testing process.
  - Establishing a dedicated staging environment that mirrors the production environment to catch such errors before deployment.
- **Tasks:**
  - Review and enhance all SQL queries in the recent updates for performance optimization.
  - Establish automated rollback mechanisms for quickly reverting faulty deployments.
  - Increase monitoring granularity to detect and alert on unusual database activities.
  - Train developers on best practices for database design and query optimization.

This incident underscores the importance of robust testing environments and deployment protocols to prevent similar occurrences in the future. The new staging environment setup and improved monitoring will help in early detection and mitigation of issues that could impact user experience.
