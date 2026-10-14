# Deployment Checklist

**Method:** local install / network-server / web / cloud (PaaS) / container / mobile
**Environment:** dev / staging / production · **Version:**

## Before
- [ ] All tests pass in CI
- [ ] CHANGELOG and release notes updated; version tagged in Git
- [ ] Config held in environment variables (no secrets in the repo)
- [ ] Database backup taken; migration scripts tested
- [ ] Rollback plan written

## Deploy
- [ ] Steps followed (list them)
- [ ] Smoke test on the deployed version

## After
- [ ] Monitoring and logs checked
- [ ] Users informed (release notes)
- [ ] Deployment recorded in the development log
