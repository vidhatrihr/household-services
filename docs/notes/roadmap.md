# roadmap [done 🤗✅]

admin block/approve customers (optional)

- Customer.is_approved=True
- or User.is_approved=True
- =True means customers are by default approved
- GET `/admin/approve-customer/<customer_id>`
- GET `/admin/block-customer/<customer_id>`

professionals/customers (required)

- view profile
  - GET `/professional/profile`, professional_profile.html
  - GET `/customer/profile`, customer_profile.html
- edit profile
  - GET, POST `/customer/edit-profile`, customer_edit_profile.html
  - GET, POST `/professional/edit-profile`, professional_edit_profile.html
