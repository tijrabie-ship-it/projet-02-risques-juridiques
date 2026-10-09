import streamlit as st

st.set_page_config(page_title="نظام التدقيق القانوني", page_icon="📜")

st.title("📜 نظام التدقيق القانوني للمرابحة")
st.write("---")

st.header("أولاً: التدقيق في الوثائق المادية")
notary_certified = st.checkbox("العقد موثق لدى جهة مختصة (موثق/عدل)")
tax_stamped = st.checkbox("تم أداء رسوم التسجيل والتمبر (Sceau)")

st.header("ثانياً: التحقق من القوة القانونية")
exec_clause = st.checkbox("العقد يتضمن صيغة 'القوة التنفيذية' (Force Exécutoire)")
jurisdiction_clause = st.checkbox("بند 'فض النزاعات' يحدد المحاكم المغربية اختصاصاً أصلياً")

if st.button("إصدار التقرير القانوني"):
    all_doc_ok = notary_certified and tax_stamped
    all_legal_ok = exec_clause and jurisdiction_clause
    
    if all_doc_ok and all_legal_ok:
        st.balloons()
        st.success("✅ العقد محصن قانونياً: جميع الوثائق مكتملة والقوة التنفيذية متوفرة.")
    elif all_doc_ok and not all_legal_ok:
        st.warning("⚠️ العقد صحيح وثائقياً، لكنه يفتقر للتحصين القانوني (صيغة التنفيذ).")
    else:
        st.error("❌ مخاطر قانونية عالية: العقد غير مكتمل، يرجى مراجعة القسم القانوني فوراً.")

st.sidebar.info("هذا النظام مخصص للتحقق من حصانة العقود وفقاً للقوانين المنظمة للتمويلات التشاركية في المغرب.")
st.subheader("🛠️ وحدة التحصين القانوني (القوة التنفيذية)")

is_notarized = st.checkbox("هل العقد محرر من طرف موثق أو عدل؟")
has_exec_clause = st.checkbox("هل يتضمن العقد بند 'القوة التنفيذية' صراحة؟")
is_registered = st.checkbox("هل تم التسجيل لدى إدارة الضرائب (التمبير)؟")

# منطق تقييم القوة التنفيذية
if st.button("تقييم القوة التنفيذية"):
    if is_notarized and has_exec_clause and is_registered:
        st.success("✅ العقد يتمتع بقوة تنفيذية كاملة (سند تنفيذي).")
        st.write("يمكن للمصرف في حالة التعثر البدء في إجراءات التنفيذ الجبري فوراً.")
    else:
        st.error("⚠️ تحذير: العقد يفتقر لمقومات السند التنفيذي.")
        st.write("نصيحة: يجب إضافة بند القوة التنفيذية وتوثيق العقد لضمان سرعة التحصيل.")