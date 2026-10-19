# CodeAlpha - Secure Coding Review

## Project Overview
This project reviews a sample Python login program
to identify common security weaknesses.

## Vulnerability 1: Hardcoded Credentials
**Issue:** Username and password are stored directly
in the source code.

**Risk:** Anyone with access to the source file can
read the credentials.

**Recommendation:** Never hardcode real credentials.
Use secure configuration and an appropriate
authentication system.

## Vulnerability 2: Unlimited Login Attempts
**Issue:** The example has no limit on login attempts.

**Risk:** Repeated password guessing is not restricted.

**Recommendation:** Implement appropriate attempt
limits and additional protections in a real application.

## Vulnerability 3: Plaintext Password Storage
**Issue:** The password is stored in readable text.

**Risk:** Exposed credentials can be read directly.

**Recommendation:** Use a suitable password-hashing
algorithm such as Argon2id or scrypt.

## Conclusion
This review identifies basic authentication weaknesses
and recommends safer practices.