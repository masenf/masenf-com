:title sql saves the day
:author masen
:published 1365105517
:modified 1365105517
:slug sql-saves-the-day
:tag technical short

Finally cracked the nut on a problem I've been working on: trying to determine from a
login event and a record of logins and logouts whether that login event
constitutes the beginning of a concurrent session for the given user. Trying to
solve this problem using backtracking is a lot of effort and brushes up against
the halting problem. In this method, we simply look backwards at logins and
logouts from the event being inspected until we can determine if there is an
overlapping session. The problem here is that there is no promise that such an
algorithm will complete in reasonable time. This is not a solution.

After a bit more thought, I realized that we're trying to find out something
about the cross product between logins and logouts. I was able to formulate
this nice SQL query which returns sessions active for ``@USER`` at the time
``@TS``

.. code:: mysql

    SELECT li.sessionId, 
           li.ts as loginTime, 
           lo.ts as logoutTime, 
           li.username as user 
    FROM LoginEvent as li 
    LEFT OUTER JOIN LogoutEvent as lo 
        ON li.sessionId = lo.sessionId 
    WHERE  li.ts <= @TS AND 
           (lo.ts >= @TS OR lo.ts IS NULL) AND 
           li.username = @USER;
